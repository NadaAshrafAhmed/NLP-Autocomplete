import codecs

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fill/<string:input>')
def fill(input):
    input = input[0:len( input ) - 1]
    temp=input
    temp="@ @ "+input
    s=temp.split(' ')
    res=[]
    # if (s[len( s ) - 2], s[len( s ) - 1]) in lookUpTable:
    #     for i in lookUpTable[(s[len( s ) - 2], s[len( s ) - 1])]:
    #         temp = i
    #         temp = input + " " + i
    #         res += [temp]
    if(input[len(input)-1]==' '):
        if (s[len(s)-3],s[len(s)-2]) in lookUpTable:
            for i in lookUpTable[(s[len(s)-3],s[len(s)-2])]:
                temp=i
                temp=input+i
                res+=[temp]
    else:
        if (s[len(s)-3],s[len(s)-2]) in lookUpTable:
            input1 = input[0:len( input ) - len(s[len(s)-1])]
            for i in lookUpTable[(s[len(s)-3],s[len(s)-2])]:
                if (i.startswith(s[len(s)-1]) and i!=s[len(s)-1]):
                    temp=i
                    temp=input1+i
                    res+=[temp]

        if(len(res)==0):
            if (s[len( s ) - 2], s[len( s ) - 1]) in lookUpTable:
                for i in lookUpTable[(s[len( s ) - 2], s[len( s ) - 1])]:
                    temp = i
                    temp = input+" "+ i
                    res += [temp]
    res=str(res)
    res=res.replace("'", '"')
    return (res)

lookUpTable={}

def init():
    f = codecs.open( "res.txt", encoding='utf-8' )
    y=f.readline()
    y = y[0:len( y ) - 1]
    y=int(y)
    for j in range(0,y):
        s1=f.readline()
        s2=f.readline()
        s1=s1[0:len(s1)-1]
        s2=s2[0:len(s2)-1]
        lookUpTable[(s1,s2)]=[]
        x=f.readline()
        x = x[0:len( x ) - 1]
        n=int(x)

        for i in range(0,n):
            # f.readline() #probability
            ch=f.readline()
            ch = ch[0:len( ch ) - 1]
            lookUpTable[(s1, s2)] += [ch]

    f.close()

if __name__ == '__main__':
    init()
    app.run(debug=True)