template = '../run_gem5_alpha_spec06_benchmark.sh -b "{}\;{}"' + \
        ' -o {}/{} -s --smt -v fast -a ALPHA_{}'

#conf = 'DYN'
conf = 'CC'
#odir = '~/hard'
#odir = '~/dyn_96_SQ'
odir = '~/sim_st_64_lsq'
# inf = 'rand.txt'
inf = 'sim_st.txt'
#inf = 'hard.txt'

with open(inf) as f, open('./select.sh', 'w') as of:
    for line in f:
        t1, t2 = line.split()
        cmd = template.format(t1, t2, odir, t1 + '_' + t2, conf)
        of.write(cmd+'\n')
        print cmd


print 'generate run scripts from', inf, 'with arch', conf, 'to dir', odir
