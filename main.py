from dfsjson.src.dfsjson import DFSJson

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Create a complex JSON object
    example_json = """{
        "key1": "value1'
        "key2": [1 2, 3]
        "key3":  {
            "subkey1": "subvalue1"
            "subkey2": "subvalue2"
        ,
    }"""

    rj = DFSJson(max_depth=100, max_diff=10)
    print(rj.loads(example_json))
