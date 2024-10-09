import os

vars = os.environ
out = []
env_var = []
for var, val in vars.items():
    out.insert(0, f"{var}^{val}")
#print(out)
for i in out:
    env_var.append(str(i))
#print(env_var)

def environment_var(text:str) -> str:
    txt = text
    for i in list(env_var):
        var = str(i).lower().split("^")
        
        if "%" + var[0] + "%" in txt:
            txt = txt.replace("%" + var[0] + "%", var[1].replace("\\", "\\\\"))
    return fr"{txt}"

    
if __name__ == "__main__":
    print(environment_var("%appdata%"))
