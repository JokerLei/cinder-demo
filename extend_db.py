from cinder.db.sqlalchemy import api, models


def delete_volume_glance_metadata(volume):
    session = api.get_session()

    with session.begin():
        session.query(models.VolumeGlanceMetadata) \
            .filter_by(volume_id=volume.id).delete()
