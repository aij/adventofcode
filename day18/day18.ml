#!/usr/bin/env ocaml

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

Printf.printf "Surface area: %d\n" surface_area;;
