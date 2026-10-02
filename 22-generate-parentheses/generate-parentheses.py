class Solution(object):

    def generateParenthesis(self, pairs):

        ans = []

        def cook(combo, openVibe, closeVibe):

            if len(combo) == pairs * 2:
                ans.append(combo)
                return

            if openVibe < pairs:
                cook(combo + "(", openVibe + 1, closeVibe)

            if closeVibe < openVibe:
                cook(combo + ")", openVibe, closeVibe + 1)

        cook("", 0, 0)
        return ans