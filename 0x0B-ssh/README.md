# SSH: 0x0B-ssh

SSH is a secure protocol that's mainly used to connect linux servers remotely through a text-based interface. This protocol allows you to connect to a remote server and execute your commands directly on your local terminal.

## How to generate SSH Key Pairs

You can use RSA, DSA, and ECDSA cryptographic algorithims to generate your SSH keys. Generally, RSA keys are preferred, and you can use the following command to generate them on your local machine:

<code> $ ssh-keygen </code>

Then you get the following prompt, which allows you to enter the location to store your RSA private key:

<code> Generating public/private rsa key pair.
Enter file in which to save the key (/home/demo/.ssh/id\_rsa):</code>

You will also get a prompt to enter a passprase that you will use each time you use the private key. Leave it blank and press Enter if you do not need the passphrase.

After this process, your RSA SSH key pair will be generated. The private key will be saved in ~/.ssh/id\_rsa and the associated public key in ~/.ssh/id\_rsa.pub by default.


