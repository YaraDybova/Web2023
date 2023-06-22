from models import Cover
import hashlib
import uuid
import os
from werkzeug.utils import secure_filename
from app import db, app

class ImageSaver:
    def __init__(self, file):
        self.file = file

    def save(self):
        self.img = self.__find_by_md5_hash()
        if self.img is not None:
            return self.img
        file_name = secure_filename(self.file.filename)
        self.img = Cover(
            file_name=file_name,
            mime_type=self.file.mimetype,
            md5_hash=self.md5_hash)
        db.session.add(self.img)
        db.session.commit()
        self.file.save(
            os.path.join(app.config['UPLOAD_FOLDER'],
            self.img.storage_filename)
        )
        return self.img

    def __find_by_md5_hash(self):
        self.md5_hash = hashlib.md5(self.file.read()).hexdigest()
        self.file.seek(0)
        return Cover.query.filter(Cover.md5_hash == self.md5_hash).first()