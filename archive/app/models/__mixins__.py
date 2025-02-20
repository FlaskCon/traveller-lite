from app.extensions import db


class MetaMixins:
    @classmethod
    def __is_empty__(cls) -> bool:
        """
        Returns True if the table is empty, False otherwise.
        :return:
        """
        return (
            True
            if db.session.execute(db.select(cls).limit(1)).scalar_one_or_none() is None
            else False
        )
