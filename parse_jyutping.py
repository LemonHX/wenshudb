def parse_jyutping(jyutping):
    # what the fuck
    if len(jyutping) < 2:
        raise ValueError("Jyutping string too short")
    init = ""
    if jyutping[0] == 'n' and jyutping[1] == 'g' and len(jyutping) == 3:
        init = ""
    elif jyutping[0] == 'm' and len(jyutping) == 2:
        init = ""
    elif jyutping[0] == 'n' and jyutping[1] == 'g':
        init = 'ng'
        jyutping = jyutping[1:]
    elif jyutping[0] == 'g' and jyutping[1] == 'w':
        init = 'gw'
        jyutping = jyutping[1:]
    elif jyutping[0] in 'bpmfdtnlgkhwzcsj':
        init = jyutping[0]
        jyutping = jyutping[1:]
    else:
        jyutping = jyutping
    try:
        tone = int(jyutping[-1])
        jyutping = jyutping[:-1]
    except:
        raise ValueError("Jyutping string does not end with a tone number")
    finals = jyutping
    last = ""
    if finals[-1] in "ptk":
        last = finals[-1]
        finals = finals[:-1]
        return [init, finals, last, tone]
    else:
        return [init, finals, last, tone]

if __name__ == "__main__":
    import sys
    print(parse_jyutping(sys.argv[1]))