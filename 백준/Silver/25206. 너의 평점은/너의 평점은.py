rating = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0]
grade = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F']


total=0 #학점의 총합
result =0 #학점 * 과목평점


for i in range(20):
    subject, r, g = input().split()
    r = float(r)
    if g != 'P':
        total += r
        result += r * rating[grade.index(g)]

print('%.6f' % (result / total))

