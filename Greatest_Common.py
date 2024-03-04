def greatest_common(a,b):
    if a>b:
        last=a%b
        while last != 0:
            lsat = b % last
    else:
        last=b%a
        while last!=0:
            lsat=a%last
            greatest_common()