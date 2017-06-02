fileName = '2017-05-27-11-55-20-robot-joint_states'
with open(fileName+'.csv') as f, open(fileName+'_postproc.csv', 'w') as f2:
    for x in f:
        if 'finger_joint' not in x:
            f2.write(x.strip()+'\n')  