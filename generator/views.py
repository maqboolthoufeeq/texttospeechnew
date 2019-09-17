from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

unitlist = ['', 'ONE ', 'TWO ', 'THREE ', 'FOUR ', 'FIVE ', 'SIX ',
            'SEVEN ', 'EIGHT ', 'NINE ', 'TEN ', 'ELEVEN ', 'TWELVE ',
            'THIRTEEN ', 'FOURTEEN ', 'FIFTEEN ', 'SIXTEEN ', 'SEVENTEEN ', 'EIGHTEEN ', 'NINETEEN ']
tylist = ['', '', 'TWENTY ', 'THIRTY ', 'FOURTY ',
          'FIFTY ', 'SIXTY ', 'SEVENTY ', 'EIGHTY ', 'NINETY ']
extlist = ['HUNDRED ', 'THOUSAND ', 'LAKH ', 'CRORE ']


def wordwrap(request, inum):
    numword = ''
    if(inum == 0):
        numword = 'ZERO'
        return numword
    elif(inum == 1000000000):
        numword = 'ONE BILLION'
        return numword
    else:
        numword = numword + check(request, inum//10000000, extlist[3])
        numword = numword + check(request, ((inum//100000) % 100), extlist[2])
        numword = numword + check(request, ((inum//1000) % 100), extlist[1])
        numword = numword + check(request, ((inum//100) % 10), extlist[0])

        if(inum > 100 and inum % 100):
            numword = numword + "AND "

        numword = numword + check(request, (inum % 100), "")

        return numword


def check(request, finum, fword):

    cword = ""

    if(finum > 19):
        cword = cword + tylist[finum//10]+unitlist[finum % 10]
    else:
        cword = cword + unitlist[finum]
    if(finum >= 1):
        cword = cword+fword

    return cword


def checker(request):
    if request.method == 'GET':
        innum = request.GET['inputnum']
        inum = int(innum)
        inum = abs(inum)
        sinum = str(inum)
        if(inum > 1000000000):
                flag = "Number Exeed Limit, (Limit upto : 1000000000)"
                return render(request, 'generator/index.html', {'flag': flag, 'inum': inum})
        else:
                flag = wordwrap(request, inum)
                return render(request, 'generator/index.html', {'flag': flag, 'inum': inum})


def index(request):

    return render(request, 'generator/index.html')
