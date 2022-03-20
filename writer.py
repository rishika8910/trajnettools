import json
from .data import PygameSceneRow, PygameTrackRow


def trajnet_tracks(row):
    x = round(row.x, 2)
    y = round(row.y, 2)
    if row.prediction_number is None:
        return json.dumps({'track': {'f': row.frame, 'p': row.pedestrian, 'x': x, 'y': y, 'group': row.group, 'obstacles': row.obstacles}})
    return json.dumps({'track': {'f': row.frame, 'p': row.pedestrian, 'x': x, 'y': y,
                                 'prediction_number': row.prediction_number,
                                 'scene_id': row.scene_id}})



def trajnet_scenes(row):
    return json.dumps(
        {'scene': {'id': row.scene, 'p': row.pedestrian, 's': row.start, 'e': row.end, 'group': row.group,
                   'fps': row.fps, 'obstacles': row.obstacles}})


def trajnet(row):
    if isinstance(row, PygameTrackRow):
        return trajnet_tracks(row)
    if isinstance(row, PygameSceneRow):
        return trajnet_scenes(row)

    raise Exception('unknown row type')