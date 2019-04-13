'''
:Authors:         Shashank Agrawal
:Date:            5/2016
'''

from charm.toolbox.pairinggroup import PairingGroup, GT
from cgw15 import CGW15CPABE
import time
import sys

def main(attribute = None):
    # instantiate a bilinear pairing map
    pairing_group = PairingGroup('MNT224')
  
    # AC17 CP-ABE under DLIN (2-linear)
    cpabe = CGW15CPABE(pairing_group, 2)

    # run the set up
    (pk, msk) = cpabe.setup()
    i = 0
    policy_str = ''
    # generate a key
    attr_list = []
    while i < int(attribute):
       i= i+1
       attr_list.append('A'+str(i))
       if i == 1:
          policy_str = 'A1'
       else:
          policy_str = policy_str + ' and A' + str(i)
    f = open("keygen"+str(attribute)+"cgw15.csv","w")
    f.write("time(sec)\n")
    for _ in  range(1000):
        startTime = time.time()
        key = cpabe.keygen(pk, msk, attr_list)
        f.write(str(time.time() - startTime)+"\n")
    # choose a random message
    msg = pairing_group.random(GT)
   
    # generate a ciphertext
    f = open("enc"+str(attribute)+"cgw15.csv","w")
    f.write("time(sec)\n")
    for _ in  range(1000):
        startTime = time.time()
        ctxt = cpabe.encrypt(pk, msg, policy_str)
        f.write(str(time.time() - startTime)+"\n")

    # decryption
    f = open("dec"+str(attribute)+"cgw15.csv","w")
    f.write("time(sec)\n")
    for _ in  range(1000):
        startTime = time.time()
        rec_msg = cpabe.decrypt(pk, ctxt, key)
        f.write(str(time.time() - startTime)+"\n")
   
    print(sys.getsizeof(ctxt))
    ''' if debug:'''
    if rec_msg == msg:
            print ("Successful decryption.")
    else:
            print ("Decryption failed.")


if __name__ == "__main__":
    debug = True
    sys.exit(main(*sys.argv[1:]))
