# coding=utf-8
from datetime import datetime
from model import db

class User(db.Model):
    """

    """
    __tablename__ = 'users'
    uid = db.Column(db.Integer, primary_key=True)
    place = db.Column(db.String, nullable=False)
    status = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

    @staticmethod
    def set_config(uid, place, status):
        """Guarda un valor

        Args:
            :param uid: Id. del usuario
            :param place: lugar del usuario
            :param status: Valor del estado del usuario

        Returns:
            :return: Instancia del usuario con los el valor almacenado
        """
        record = db.session.query(User).first()

        if record is None:
            record = User(uid=uid, place=place, status=status, created_at=datetime.now())
            db.session.add(record)
        else:
            record.status = status
            record.place = place
            record.created_at = datetime.now()

        db.session.commit()
        db.session.close()

        return record

    @staticmethod
    def get_config(chat, key):
        """ Recupera un valor

        Args:
            :param chat: Id. del chat
            :param key: Clave del valor a recuperar

        Returns:
            :return: Instancia de Chat que coincide con la clave o None si no existe
        """
        record = db.session.query(Chat).filter_by(chat=chat, key=key).first()
        db.session.close()

        return record


