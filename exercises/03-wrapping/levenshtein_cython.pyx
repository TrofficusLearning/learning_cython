cdef extern from "levenshtein.h":
    int levenshtein_dist(const char *s, const char *t)

def levenshtein_distance(char *s, char *t):
    return levenshtein_dist(s, t)
