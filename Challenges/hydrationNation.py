#hydrationNation
def oplossing(string, ending):
    begin = len(string) - len(ending)
    einde = string[begin:]
    if einde == ending:
        return True
    else:
        return False