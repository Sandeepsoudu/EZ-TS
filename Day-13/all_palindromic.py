def main():
    _str="madammadam"
    n=len(_str)
    dp=[[0 for i in range(n)] for j in range(n)]
    i,j=0,0
    while j<n:
        jflag=j
        while jflag<n:
            if i==jflag:
                dp[i][jflag]=1
            
            if abs(i-jflag)==2:
                if _str[i]==_str[jflag]
        j+=1
        i=0
