import os
import pprint

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


def seed_params(seed_num, mapper):
    params = {}
    map_soil = [get_delta(
        seed_num, x['source'], x['destination']
    ) for x in mapper['seed_to_soil']]
    soil = list(filter(None, map_soil))
    params['soil'] = soil[0] if len(soil) > 0 else seed_num

    map_fertilizer = [get_delta(
        params['soil'], x['source'], x['destination']
    ) for x in mapper['soil_to_fertilizer']]
    fertilizer = list(filter(None, map_fertilizer))
    params['fertilizer'] = fertilizer[0] if len(fertilizer) > 0  \
        else params['soil']

    map_water = [get_delta(
        params['fertilizer'], x['source'], x['destination']
    ) for x in mapper['fertilizer_to_water']]
    water = list(filter(None, map_water))
    params['water'] = water[0] if len(water) > 0 \
        else params['fertilizer']

    map_light = [get_delta(
        params['water'], x['source'], x['destination']
    ) for x in mapper['water_to_light']]
    light = list(filter(None, map_light))
    params['light'] = light[0] if len(light) > 0 \
        else params['water']

    map_temperature = [get_delta(
        params['light'], x['source'], x['destination']
    ) for x in mapper['light_to_temp']]
    temperature = list(filter(None, map_temperature))
    params['temperature'] = temperature[0] if len(temperature) > 0 \
        else params['light']

    map_humidity = [get_delta(
        params['temperature'], x['source'], x['destination']
    ) for x in mapper['temp_to_humidity']]
    humidity = list(filter(None, map_humidity))
    params['humidity'] = humidity[0] if len(humidity) > 0 \
        else params['temperature']

    map_location = [get_delta(
        params['humidity'], x['source'], x['destination']
    ) for x in mapper['humidity_to_location']]
    location = list(filter(None, map_location))
    params['location'] = location[0] if len(location) > 0 \
        else params['humidity']

    return params


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
        'seed_to_soil': seed_to_soil_map,
        'soil_to_fertilizer': soil_to_fert_map,
        'fertilizer_to_water': fert_to_water_map,
        'water_to_light': water_to_light_map,
        'light_to_temp': light_to_temp_map,
        'temp_to_humidity': temp_to_hum_map,
        'humidity_to_location': hum_to_loc_map,
    }, seeds]


with open(input_file, encoding="utf-8") as i_file:
    seed_mapper = i_file.read()
    raw_map, seeds = get_raw(seed_mapper)
    set_map = {k: [set_interval(x) for x in v] for (k, v) in raw_map.items()}
    seed_props = [seed_params(x, set_map) for x in seeds]
    seed_props.sort(key=lambda seed: seed['location'])
    pprint.pprint(seed_props[0]['location'])
    i_file.close()
