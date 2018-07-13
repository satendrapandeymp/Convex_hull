reset

#set decimalsign ','

set grid ytics mytics mxtics
set mytics 2
set mxtics 5
set grid ytics lc rgb "#bbbbbb" lw 2 lt 0
set grid xtics lc rgb "#bbbbbb" lw 2 lt 0

set ylabel "probability of getting stuck"
set xlabel "Area fraction"

set title "{/:Bold probability of getting stuck vs Area fraction}"

plot 'data.txt' using 1:2:3 with circle title '', '' using 1:2:4 with labels title "" offset 0,char .8

pause -1
