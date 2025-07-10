#Feature
- notifi batterai
- notif internet
- Full dinamy promt
- tampilan ala hacker profesional
- real-time status
- full termux API
- efek matrix startup
- auto-lock login  page mode siluman
- modify PS1 variable
- efek crash login denied terminal auto logout
- header proffesional full color
- welcome page dinamis

#Tools
- nano pkg install nano          
- figlet pkg install figlet
- lolcat pkg install lolcat
- Jq pkg install jq
- Termux-API  pkg install termux-ap
- cmatrix


#installation prompt
  pkg update && pkg upgrade
  pkg install nano -y
  pkg install figlet 
  pkg install lolcat 
  pkg install jq -y
  pkg install termux-api -y
  pkg install cmatrix 

##step by step
  #steps 1 
  1. buka termux kemudian cari file .bashrc, secara default lokasinya ada pada ~/data/data/com.termux/files/home ".bashrc" dapat di lihat dengan mengetikkan perintah : "bash ls -a"
  2. next ketik perintah "nano .bashrc" yang akan membawah kita masuk ke editor text pada file .bashrc. nah pada file ini kita akan memulai memodifikasi tampilan termux dengan membuat ulang prompt dengan tools yang telah kita install tadi
  3. tekan CTRL + K untuk membersihkan agar lebih rapih & nyaman.
  4. setiap kali menambah/mengedit command baru maka harus menyimpannya dengan CTRL + S. kemudian untuk keluar dari mode editor text tekan CTRL + X
  
  #steps 2 
  1.edit PS1 agar tampilan lebih dinamis #PROMPT DINAMIS ULTRA
    PROMPT_COMMAND='check_notify;
    export PS1="\[\e[38;5;46m\]╭─[\[\e[1;37m\]\u@\h \[\e[38;5;4 4m\]\d \t \[\e[38;5;198m\]\w\[\e[0m\]\[\e[38;5;46m\]]\n"
    export PS1+="│ IP: \[\e[1;36m\]\$(get_ip)  \[\e[33m\]BAT: \ [\e[1;32m\]\$(get_batt)% \[\e[35m\](\$(get_charger)) \[\e[3 6m\]NET: \$(get_net_status)\n"
    export PS1+="\[\e[38;5;46m\]╰──λ \[\e[1;35m\]\$(get_emoji) \[\e[0m\]"
    '

  