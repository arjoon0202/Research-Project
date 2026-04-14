import re
from collections import Counter

def check_segment(text):
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    sentences = [s for s in sentences if len(s.split()) >= 3]
    results = {}

    ai_words = [
        'delve','delves','delving','comprehensive','crucial','pivotal',
        'nuanced','multifaceted','robust','landscape','tapestry','realm',
        'interplay','illuminate','elucidate','underscore','underscores',
        'navigate','foster','intricate','intricacies','meticulous',
        'meticulously','paramount','testament','groundbreaking','holistic',
        'synergy','furthermore','moreover','additionally','facilitate',
        'enhance','bolster','noteworthy','showcasing','showcases','embark',
        'endeavor','endeavour','vibrant','dynamic','seamless','seamlessly',
        'elevate','elevates'
    ]
    text_lower = text.lower()
    found_ai = [w for w in ai_words if w in text_lower]
    vocab_count = len(found_ai)
    results['vocab'] = vocab_count <= 2
    results['vocab_count'] = vocab_count
    results['vocab_found'] = found_ai

    lengths = [len(s.split()) for s in sentences]
    if len(lengths) >= 2:
        mean_len = sum(lengths) / len(lengths)
        variance = sum((x - mean_len)**2 for x in lengths) / len(lengths)
        sd = variance ** 0.5
    else:
        sd = 0
    results['sent_sd'] = sd > 8
    results['sent_sd_val'] = round(sd, 1)
    results['sent_lengths'] = lengths

    openers = [s.split()[0] for s in sentences if s.split()]
    opener_counts = Counter(openers)
    max_opener = max(opener_counts.values()) if opener_counts else 0
    results['openers'] = max_opener <= 2
    results['openers_max'] = max_opener
    results['openers_detail'] = dict(opener_counts)

    paragraphs = [p.strip() for p in text.split('\n') if p.strip()]
    para_lengths = [len(p.split()) for p in paragraphs]
    if len(para_lengths) >= 2:
        min_p, max_p = min(para_lengths), max(para_lengths)
        variance_pct = ((max_p - min_p) / max_p * 100) if max_p > 0 else 0
    else:
        variance_pct = 0
    results['para_var'] = variance_pct >= 30
    results['para_var_val'] = round(variance_pct, 1)
    results['para_count'] = len(para_lengths)
    results['para_lengths'] = para_lengths

    banned = ['furthermore', 'moreover', 'additionally']
    para_openers = [p.strip().split()[0].lower().rstrip(',') for p in paragraphs if p.strip()]
    banned_count = sum(1 for o in para_openers if o in banned)
    results['transitions'] = banned_count == 0
    results['transitions_count'] = banned_count

    rot_pattern = r'\b\w+,\s+\w+,\s+and\s+\w+'
    rot_matches = re.findall(rot_pattern, text)
    results['rot'] = len(rot_matches) <= 1
    results['rot_count'] = len(rot_matches)
    results['rot_matches'] = rot_matches

    meta_phrases = [
        'this section will', 'this section examines',
        'this chapter will', 'this chapter examines',
        'as discussed in section', 'as noted in section',
        'applying the .* lens', 'through the lens of',
        'this section has shown', 'this chapter has demonstrated'
    ]
    meta_count = sum(1 for p in meta_phrases if re.search(p, text_lower))
    results['meta'] = meta_count == 0
    results['meta_count'] = meta_count

    checks = ['vocab','sent_sd','openers','para_var','transitions','rot','meta']
    score = sum(1 for c in checks if results[c])
    results['score'] = score
    results['pass'] = score >= 6
    return results

def print_results(results, label=""):
    print(f"\n{'='*50}")
    if label:
        print(f"  {label}")
    print(f"{'='*50}")
    print(f"  1. Vocab:      {'PASS' if results['vocab'] else 'FAIL'} (count={results['vocab_count']}, found={results.get('vocab_found',[])})")
    print(f"  2. Sent SD:    {'PASS' if results['sent_sd'] else 'FAIL'} (SD={results['sent_sd_val']}, lengths={results['sent_lengths']})")
    print(f"  3. Openers:    {'PASS' if results['openers'] else 'FAIL'} (max={results['openers_max']}, detail={results['openers_detail']})")
    print(f"  4. Para Var:   {'PASS' if results['para_var'] else 'FAIL'} (variance={results['para_var_val']}%, count={results['para_count']}, lengths={results['para_lengths']})")
    print(f"  5. Transitions:{'PASS' if results['transitions'] else 'FAIL'} (banned={results['transitions_count']})")
    print(f"  6. Rule-of-3:  {'PASS' if results['rot'] else 'FAIL'} (count={results['rot_count']}, matches={results['rot_matches']})")
    print(f"  7. Meta:       {'PASS' if results['meta'] else 'FAIL'} (count={results['meta_count']})")
    print(f"  SCORE: {results['score']}/7 {'** PASS **' if results['pass'] else '** FAIL **'}")
    print(f"{'='*50}")
