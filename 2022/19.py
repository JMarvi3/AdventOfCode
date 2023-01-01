from functools import cache
from current_puzzle import current_puzzle
import aoc_lib


class Blueprint:
    def __init__(self, num, ore_ore, clay_ore, obs_ore, obs_clay, geo_ore, geo_obs):
        self.num = num
        self.ore_ore = ore_ore
        self.clay_ore = clay_ore
        self.obs_ore = obs_ore
        self.obs_clay = obs_clay
        self.geo_ore = geo_ore
        self.geo_obs = geo_obs
        self.max_ore = max(ore_ore, clay_ore, obs_ore, geo_ore)
        self.max_clay = obs_clay
        self.max_obs = geo_obs

    def __repr__(self):
        return f"{self.num}: ore: {self.ore_ore} ore, clay: {self.clay_ore} ore, obsidian: {self.obs_ore} ore and {self.obs_clay} clay, geode: {self.geo_ore} ore and {self.geo_obs} obsidian (maxes: {self.max_ore, self.max_clay, self.max_obs})"

    def buy_ore(self, ore, clay, obs, ore_bots, clay_bots, obs_bots):
        return ore >= self.ore_ore and ore_bots < self.max_ore

    def buy_clay(self, ore, clay, obs, ore_bots, clay_bots, obs_bots):
        return ore >= self.clay_ore and clay_bots < self.max_clay

    def buy_obs(self, ore, clay, obs, ore_bots, clay_bots, obs_bots):
        return ore >= self.obs_ore and clay >= self.obs_clay and obs_bots < self.max_obs

    def buy_geo(self, ore, clay, obs, ore_bots, clay_bots, obs_bots):
        return ore >= self.geo_ore and obs >= self.geo_obs

    @cache
    def calc(self, max_min=24,
             ore=0, clay=0, obs=0, geo=0, ore_bots=1, clay_bots=0, obs_bots=0, geo_bots=0, t=0, seen=None):
        if seen is None:
            seen = set()
        if t == max_min:
            return geo

        ore = min(ore, self.max_ore * 2)
        clay = min(clay, self.max_clay * 2)
        obs = min(obs, self.max_obs * 2)
        geo += geo_bots
        t += 1
        best = self.calc(max_min,
                         ore + ore_bots, clay + clay_bots, obs + obs_bots, geo,
                         ore_bots, clay_bots, obs_bots, geo_bots, t)
        if self.buy_ore(ore, clay, obs, ore_bots, clay_bots, obs_bots):
            best = max(best, self.calc(max_min,
                                       ore + ore_bots - self.ore_ore, clay + clay_bots, obs + obs_bots, geo,
                                       ore_bots + 1, clay_bots, obs_bots, geo_bots, t))
        if self.buy_clay(ore, clay, obs, ore_bots, clay_bots, obs_bots):
            best = max(best, self.calc(max_min,
                                       ore + ore_bots - self.clay_ore, clay + clay_bots, obs + obs_bots, geo,
                                       ore_bots, clay_bots + 1, obs_bots, geo_bots, t))
        if self.buy_obs(ore, clay, obs, ore_bots, clay_bots, obs_bots):
            best = max(best, self.calc(max_min,
                                       ore + ore_bots - self.obs_ore, clay + clay_bots - self.obs_clay, obs + obs_bots, geo,
                                       ore_bots, clay_bots, obs_bots + 1, geo_bots, t))
        if self.buy_geo(ore, clay, obs, ore_bots, clay_bots, obs_bots):
            best = max(best, self.calc(max_min,
                                       ore + ore_bots - self.geo_ore, clay + clay_bots, obs + obs_bots - self.geo_obs, geo,
                                       ore_bots, clay_bots, obs_bots, geo_bots + 1, t))
        return best


puzzle = current_puzzle()
print(puzzle.title)
input_data = puzzle.input_data
# input_data = open('19.example').read()


blueprints = []
for line in input_data.splitlines():
    blueprints.append(Blueprint(*aoc_lib.findall('{:d}', line)))

quality = 0
for blueprint in blueprints:
    quality += blueprint.num * blueprint.calc()

puzzle.answer_a = quality
print('Part1:', puzzle.answer_a)

part2_answer = 1
for blueprint in blueprints[:3]:
    geodes = blueprint.calc(32)
    part2_answer *= geodes

puzzle.answer_b = part2_answer
print('Part2:', puzzle.answer_b)
