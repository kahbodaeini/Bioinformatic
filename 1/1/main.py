glob1 = ""
glob2 = ""

input_file = open('input.txt', 'r')
Lines = input_file.readlines()

count = 0
for line in Lines:
    l = line.strip()
    if l.startswith(">") and count == 0:
        count += 1
        continue
    elif not l.startswith(">") and count == 1:
        glob1 += l
        continue
    elif l.startswith(">") and count == 1:
        count += 1
        continue
    elif not l.startswith(">") and count == 2:
        glob2 += l
        continue

input_file.close()


def min_edit_dis(s1, s2, n, m, dp):
    global glob1
    global glob2

    if n == 0:
        return m
    if m == 0:
        return n

    if dp[n][m] != -1:
        return dp[n][m]

    if s1[n - 1] == s2[m - 1]:
        if dp[n - 1][m - 1] == -1:
            dp[n][m] = min_edit_dis(s1, s2, n - 1, m - 1, dp)
            return dp[n][m]
        else:
            dp[n][m] = dp[n - 1][m - 1]
            return dp[n][m]

    else:
        if dp[n - 1][m] != -1:
            m1 = dp[n - 1][m]
            glob1 = s1[:n] + '_' + s1[n:]
        else:
            m1 = min_edit_dis(s1, s2, n - 1, m, dp)
            glob2 = s2[:m] + '_' + s2[m:]

        if dp[n][m - 1] != -1:
            m2 = dp[n][m - 1]

        else:
            m2 = min_edit_dis(s1, s2, n, m - 1, dp)
        if dp[n - 1][m - 1] != -1:
            m3 = dp[n - 1][m - 1]
        else:
            m3 = min_edit_dis(s1, s2, n - 1, m - 1, dp)

        dp[n][m] = 1 + min(m1, min(m2, m3))
        return dp[n][m]


n = len(glob1)
m = len(glob2)
dp = [[-1 for i in range(m + 1)] for j in range(n + 1)]

score = min_edit_dis(glob1, glob2, n, m, dp)
print(score)
print(glob1)
print(glob2)

output_file = open("output.txt", 'w')
output_file.write(str(score))
output_file.write('\n')
output_file.write(glob1)
output_file.write('\n')
output_file.write(glob2)