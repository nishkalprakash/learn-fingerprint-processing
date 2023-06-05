## Schema of image object stored in mongoDB
{
    "_id": {
        "info": "Unique id of the image",
        "type": "BSON ObjectId",
        "required": True,
        "eg": "5f9b3b7b9c9d3b3b9c9d3b3b",
    },
    "path": {
        "info": "Path to the image",
        "type": "str",
        "required": True,
        "eg": "FVC2002/Dbs/DB1_A/100_1.tif",
    },
    "width": {
        "info":"width of the image",
        "type": "int",
        "eg":"320",
    },
    "height": {
        "info":"Height of the image",
        "type": "int",
        "eg":"66",
    },
    "image": {
        "info": "2D/3D array containing raw data the image",
        "type": "np.ndarray|list|tuple",
        "eg": "np.array([[0]*width]*height)",
    },
    "db": {
        "info":"database of the image",
        "type": "str",
        "eg":"FVC2002",
    },
    "sub_db": {
        "info":"sub database of the image (sub_db key will only exist if the db has a sub db)",
        "type": "str",
        "eg":"DB1_A",
    },
    "fin_id": {
        "info":"id of finger of the image",
        "type": "str",
        "eg":"100",
    },
    "im_id": {
        "info":"id of Impression of the image",
        "type": "str",
        "eg":"1",
    },
    "mv": {
        "info": "List of dictionaries containing the minutia info of the image, each dictionary",
        "type": "list",
        "eg": "mv = [{'x': 166, 'y': 24, 'angle': -2.4, 'type': True}, ...]",
        "mv[0]": {
            "x": "(int) x coordinate of the minutia",
            "y": "(int) y coordinate of the minutia",
            "angle": "(float) angle of the minutia in rad",
            "type": "(bool) type of the minutia (true=RE, false=Bf)",
        }
    },
    "core": {
        "info":"core points of the image, dictionary with keys as loop|delta",
        "type": "dict",
        "eg":"core = {'loop': [{'x': 124, 'y': 12},...], 'delta': [{'x': 30, 'y': 125]}}",
        "core['loop']": {
            "info":"list of dictionaries containing the loop core points",
            "type": "list",
            "eg":"core['loop'] = [{'x': 124, 'y': 12},...]",
        },
        "core['delta']": {
            "info":"list of dictionaries containing the delta core points",
            "type": "list",
            "eg":"core['delta'] = [{'x': 30, 'y': 125]}}",
        },
    },
    "mvs":{
        "info":"Minutiae extracted using a particular method as the key",
        "type":"dict",
        "eg":"mvs = {'crossing_number': mv, 'minutiae_net': mv, 'ground_truth': mv, ...}",
    },
    "cores":{
        "info":"Cores extracted using a particular method as the key",
        "type":"dict",
        "eg":"cores = {'walking': core, 'sailing': core, 'ground_truth': core, ...}",
    },
    "type":{
        "info":"Class of the fingerprint image (uses henry classification)",
        "type":"str",
        "eg":"right_loop|left_loop|whorl|arch|tented_arch",
    },
}
