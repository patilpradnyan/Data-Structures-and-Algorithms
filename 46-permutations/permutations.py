class Solution(object):
    def permute(self, nums):
        all_vibes = []
        current_vibe = []

        def cook_permutations(leftover):
            if not leftover:
                all_vibes.append(current_vibe[:])
                return

            for main_character in leftover:
                current_vibe.append(main_character)

                cook_permutations([
                    side_character
                    for side_character in leftover
                    if side_character != main_character
                ])

                current_vibe.pop()

        cook_permutations(nums)
        return all_vibes