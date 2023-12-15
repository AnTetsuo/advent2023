import os

day_01_input = "/inputs/05_input.txt"
input_path = os.getcwd()
input_file = input_path + str(day_01_input)


def get_delta(param_num, source, destination):
    bound_check = param_num in range(source[0], source[1] + 1)
    if not bound_check:
        return None
    delta = param_num - source[0]
    map_prop = delta + destination[0]
    return map_prop


def generate_seeds(seed, seed_range):
    seeds = range(seed, seed + seed_range)
    return seeds


def parse_seed(seed_list):
    seeds = []
    for ind, seed in enumerate(seed_list):
        if ind >= len(seed_list) - 1:
            break
        if ind % 2 != 0:
            continue
        seeds.append(generate_seeds(seed, seed_list[ind + 1]))
    return seeds


def set_interval(dest_source):
    ini_dest, ini_source, interval = [int(x) for x in dest_source]
    source = [ini_source, ini_source + interval - 1]
    destination = [ini_dest, ini_dest + interval - 1]
    return {
        'source': source,
        'destination': destination
    }


def get_raw(maps):
    raw_map = seed_mapper.split('\n')
    ref = list(filter(lambda x: x != '', raw_map))
    soil_ind = ref.index('seed-to-soil map:')
    fert_ind = ref.index('soil-to-fertilizer map:')
    water_ind = ref.index('fertilizer-to-water map:')
    light_ind = ref.index('water-to-light map:')
    temp_ind = ref.index('light-to-temperature map:')
    humidity_ind = ref.index('temperature-to-humidity map:')
    loc_ind = ref.index('humidity-to-location map:')
    seeds = [int(seed) for seed in ref[0].split(' ') if seed.isnumeric()]
    seed_to_soil_map = [x.split(' ') for x in ref[soil_ind + 1: fert_ind]]
    soil_to_fert_map = [x.split(' ') for x in ref[fert_ind + 1: water_ind]]
    fert_to_water_map = [x.split(' ') for x in ref[water_ind + 1: light_ind]]
    water_to_light_map = [x.split(' ') for x in ref[light_ind + 1: temp_ind]]
    light_to_temp_map = [x.split(' ') for x in ref[temp_ind + 1: humidity_ind]]
    temp_to_hum_map = [x.split(' ') for x in ref[humidity_ind + 1: loc_ind]]
    hum_to_loc_map = [x.split(' ') for x in ref[loc_ind + 1:]]
    return [{
        'humidity_to_location': hum_to_loc_map,
        'temp_to_humidity': temp_to_hum_map,
        'light_to_temp': light_to_temp_map,
        'water_to_light': water_to_light_map,
        'fertilizer_to_water': fert_to_water_map,
        'soil_to_fertilizer': soil_to_fert_map,
        'seed_to_soil': seed_to_soil_map,
    }, seeds]


def loc_by_loc(props, ranges):
    prop_list = [i for i in props.values()]
    humidity_to_location, temp_to_humidity, light_to_temp, \
        water_to_light, fertilizer_to_water, soil_to_fertilizer, \
        seed_to_soil = prop_list
    max_range = [x.stop for x in ranges]
    max_range.sort(reverse=True)
    for location in range(max_range[0]):
        param = location
        humidity = list(filter(None, [get_delta(
                        location, x['destination'], x['source'])
                        for x in humidity_to_location]))
        param = humidity[0] if len(humidity) > 0 else param

        temp = list(filter(None, [get_delta(
                    param, x['destination'], x['source'])
                    for x in temp_to_humidity]))
        param = temp[0] if len(temp) > 0 else param

        light = list(filter(None, [get_delta(
                     param, x['destination'], x['source'])
                     for x in light_to_temp]))
        param = light[0] if len(light) > 0 else param

        water = list(filter(None, [get_delta(
                     param, x['destination'], x['source'])
                     for x in water_to_light]))
        param = water[0] if len(water) > 0 else param

        fertilizer = list(filter(None,
                          [get_delta(param, x['destination'], x['source'])
                           for x in fertilizer_to_water]))
        param = fertilizer[0] if len(fertilizer) > 0 else param

        soil = list(filter(None, [get_delta(
                    param, x['destination'], x['source'])
                    for x in soil_to_fertilizer]))
        param = soil[0] if len(soil) > 0 else param

        seed = list(filter(None, [get_delta(
                    param, x['destination'], x['source'])
                    for x in seed_to_soil]))
        param = seed[0] if len(seed) > 0 else param

        any_range = [param in x for x in ranges]
        if any(any_range):
            return location


with open(input_file, encoding="utf-8") as i_file:
    seed_mapper = i_file.read()
    raw_map, seeds = get_raw(seed_mapper)
    set_map = {k: [set_interval(x) for x in v] for (k, v) in raw_map.items()}
    seed_ranges = parse_seed(seeds)
    min_location = print(loc_by_loc(set_map, seed_ranges))
    i_file.close()
