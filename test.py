import os, sys, subprocess
import show_layers

dir_path="./pj_doc"
#image_fname = "biocontainers/python-bz2file:v0.98-1-deb_cv1"
sh = show_layers.ShowHistory(20)
print(sh.run('library', 'centos', 'latest', 'sha256:a1801b843b1bfaf77c501e7a6d3f709401a1e0c83863037fa3aab063a7fdb9dc'))
#show_image_layer('library', 'centos', 'latest', 'sha256:a1801b843b1bfaf77c501e7a6d3f709401a1e0c83863037fa3aab063a7fdb9dc')
