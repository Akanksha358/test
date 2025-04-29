import re

def parse_lab_tests(text):
    result = []
    lines = text.split('\n')
    for line in lines:
        if any(c.isdigit() for c in line):
            match = re.match(r"([a-zA-Z\s]+)\s+([\d.]+)\s+([\d.-]+\s*-\s*[\d.-]+)", line)
            if match:
                name = match.group(1).strip()
                value = float(match.group(2))
                ref_range = match.group(3).strip()
                low, high = map(float, ref_range.replace(" ", "").split("-"))
                out_of_range = not (low <= value <= high)
                result.append({
                    "test_name": name,
                    "test_value": value,
                    "bio_reference_range": ref_range,
                    "lab_test_out_of_range": out_of_range
                })
    return result
