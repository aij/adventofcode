(*#!/usr/bin/env ocaml*)

let filename = "example";;

let filename = "input";;

let read_lines file =
  let contents = In_channel.with_open_text file In_channel.input_all in
  String.split_on_char '\n' (String.trim contents)
;;

let lines = read_lines filename;;


let v3 = (fun x y z -> (x,y,z))
type v3 = int * int * int

let cube_sides = [(0,0,1); (0,0,-1); (0,1,0); (0,-1,0); (1,0,0); (-1,0,0)]

let v3add (x,y,z) (a,b,c) = (x+a, y+b, z+c)

let near v = List.map (v3add v) cube_sides

let blobs : v3 list = List.map (fun s -> Scanf.sscanf s "%d,%d,%d" v3) lines;;

let cube_surface v : int = List.fold_left (fun a n -> if List.mem n blobs then a else a+1) 0 (near v);;

let surface_area : int = List.fold_left (fun a v -> a + (cube_surface v)) 0 blobs;;
(* 4314 *)

Printf.printf "Total surface area: %d\n" surface_area;;
flush stdout;;

(* Do we need to worry about bigger trapped bubbles? *)
(*
let is_surrounded v = List.for_all (fun v -> List.mem v blobs) (near v)

let cube_surface v : int = List.fold_left (fun a n -> if List.mem n blobs || is_surrounded n then a else a+1) 0 (near v);;


let surface_area2 : int = List.fold_left (fun a v -> a + (cube_surface v)) 0 blobs;;

Printf.printf "Bigger surface area: %d\n" surface_area;;
 *)

module V3 = struct
  type t = int * int * int
  let compare = compare

end

module V3Set = Set.Make(V3)

(*let cube_edges = [(0,1,1); (0,1,-1); (0,-1,1); [0,-1,-1] ... ]*)
let square_corners = [(1,1); (1,-1); (-1,1); (-1,-1)]
let cube_edges = List.flatten [
                     List.map (fun (x,y) -> (0,x,y)) square_corners;
                     List.map (fun (x,y) -> (x,0,y)) square_corners;
                     List.map (fun (x,y) -> (x,y,0)) square_corners;
                   ]
let cube_corners = List.flatten [
                     List.map (fun (x,y) -> (1,x,y)) square_corners;
                     List.map (fun (x,y) -> (-1,x,y)) square_corners;
                     List.map (fun (x,y) -> (x,1,y)) square_corners;
                     List.map (fun (x,y) -> (x,-1,y)) square_corners;
                     List.map (fun (x,y) -> (x,y,1)) square_corners;
                     List.map (fun (x,y) -> (x,y,-1)) square_corners;
                     ]
let cube_neighborhood = List.flatten [ cube_sides; cube_edges; (*cube_corners*) ];;
let neighborhood v = List.map (v3add v) cube_neighborhood

let list_count pred l = List.fold_left (fun a i -> if pred i then a+1 else a) 0 l
let list_sum l = List.fold_left (fun a i -> a + i) 0 l

(*let exterior_surface () : v3 list =*)
  let hd = List.hd blobs
  let leftmost = List.fold_left (fun ((x1,_,_) as a) ((x,_,_) as v) -> if x < x1 then v else a ) hd blobs
  let start = v3add leftmost (-1,0,0)
  let is_neighborhood v = not (List.mem v blobs) && List.exists (fun n -> List.mem n blobs) (neighborhood v)

  let rec walk visited start = List.fold_left (fun a n -> if not(is_neighborhood n) || List.mem n a then a else walk (n::a) n) visited (near start)
  let walked = walk [start] start
  let surfaces_touching v = list_count (fun n -> List.mem n blobs) (near v)

  let ext_counts = List.map surfaces_touching walked
  let ext = list_sum ext_counts

(*let ext = exterior_surface ()*)
;;Printf.printf "Walked exterior: %d\n" (List.length walked )

;;Printf.printf "Exterior surface area: %d\n" ( ext )
