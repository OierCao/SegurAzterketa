def main(textua):
    #Hiztegi bat sortu
    letrak = {}

    # Ipini letra guztiak minuskulan, erroreak saihesteko
    textua = textua.lower()
    
    letra_totalak = 0

    for char in textua:
        # letra den begiratu
        if char.isalpha():
            letra_totalak += 1
            # letra hiztegian badago, gehitu bat
            if char in letrak:
                letrak[char] += 1
            # letra hiztegian ez badago, gehitu letra eta kontatu bat
            else:
                letrak[char] = 1

    # Ordenatu letren proportzioa handienetik txikienera
    ordenean = sorted(letrak.items(), key=lambda x: x[1], reverse=True)

    # Printeatu letra eta proportzioa
    for letter, count in ordenean:
        proportion = count / letra_totalak
        print(f"{letter}: {proportion:.2%}")

textua = "RIJ AZKKZHC PIKCE XT ACKCUXJHX SZX, E NZ PEJXKE, PXGIK XFDKXNEQE RIPI RIPQEHCK ET OENRCNPI AXNAX ZJ RKCHXKCI AX CJAXDXJAXJRCEAX RTENX, E ACOXKXJRCE AXT RITEQIKERCIJCNPI OKXJHXDIDZTCNHE AX TE ACKXRRCIJ EJEKSZCNHE.AZKKZHC OZX ZJ OERHIK AX DKCPXK IKAXJ XJ XT DEDXT AX TE RTENX IQKXKE XJ REHETZJVE XJ GZTCI AX 1936. DXKI AZKKZHC, RIPI IRZKKX RIJTEN DXKNIJETCAEAXN XJ TE MCNHIKCE, JI REVI AXT RCXTI. DXKNIJCOCREQE TE HKEACRCIJ KXvITZRCIJEKCE AX TE RTENX IQKXKE. NZ XJIKPXDIDZTEKCAEA XJHKX TE RTENX HKEQEGEAIKE, KXOTXGEAE XJ XT XJHCXKKI PZTHCHZACJEKCI XJ QEKRXTIJE XT 22 AX JIvCXPQKX AX 1936,PZXNHKE XNE CAXJHCOCRERCIJ. NZ PZXKHX OZX NCJ AZAE ZJ UITDX IQGXHCvI ET DKIRXNI KXvITZRCIJEKCI XJ PEKRME. NCJ AZKKZHC SZXAI PENTCQKX XT REPCJI DEKE SZX XT XNHETCJCNPI, RIJ TE RIPDTCRCAEA AXT UIQCXKJI AXT OKXJHX DIDZTEK V AX TE ACKXRRCIJ EJEKSZCNHE,HXKPCJEKE XJ PEVI AX 1937 TE HEKXE AX TCSZCAEK TE KXvITZRCIJ, AXNPIKETCLEJAI E TE RTENX IQKXKE V OERCTCHEJAI RIJ XTTI XT DINHXKCIKHKCZJOI OKEJSZCNHE"

# deitu funtzioa
main(textua)
