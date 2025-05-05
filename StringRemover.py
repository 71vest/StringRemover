import pymem
import os
from pystyle import Center

class console:
    def __init__(this) -> None:
        this.colors = {
            "green": "\033[38;2;{};{};{}m".format(*this.hex_to_rgb("#00db3a")),
            "red": "\033[38;2;{};{};{}m".format(*this.hex_to_rgb("#bf000d")),
            "blue": "\033[38;2;{};{};{}m".format(*this.hex_to_rgb("#0095ff")),
            "cyan": "\033[38;2;{};{};{}m".format(*this.hex_to_rgb("#1cb2fc")),
            "bold": "\033[1m",
            "reset": "\033[0m"
        }

    def hex_to_rgb(this,
                    hex_color
                   ):
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

    def log(this, action: str, message: str, color: str):
        print(
            f"  {this.colors[f'{color}']}{this.colors['bold']}{action}:{this.colors['reset']}  {message}",
            flush=True
        )

    def input(this, question: str, color: str):
        print(
            f"  {this.colors[f'{color}']}{this.colors['bold']}{question}:{this.colors['reset']}",
            flush=True,
            end=" "
        )
        return input()

    def banner(this):
        print(Center.XCenter(rf"""{this.colors['cyan']}
                _   
               | |  
__   _____  ___| |_ 
\ \ / / _ \/ __| __|
 \ V /  __/\__ \ |_ 
  \_/ \___||___/\__|
                    
            {this.colors['reset']}"""), flush=True)
        
        print(Center.XCenter(f"created by vest, made for xkasti"), flush=True)
        print(Center.XCenter(f"https://neptun.wtf/"), flush=True)

class vest:
    def __init__(this) -> None:
        this.con = console()
    
    def clean(this):
        os.system('cls')
        this.con.banner()

        pid  = this.con.input("PID", "cyan")
        leng = this.con.input("LENGTH", "cyan")
        adr  = this.con.input("ADRESS", "cyan")

        pymem.memory.write_string(
            pymem.process.open(int(pid, 0)),
            int(adr, 0),
            bytes(int(leng, 0))
        )

if __name__ == "__main__":
    vest().clean()
