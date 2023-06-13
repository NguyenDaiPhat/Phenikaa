from wowf import models
from wowf.lib import fulltext
from wowf.lib.utils import get_subclasses
from wowf.scripts import BaseCommand, make_main


class UpdateIndexesCommand(BaseCommand):

    def run(self):        
        writer = fulltext.index.writer()
        for cls in get_subclasses(models, models.Base):
            if cls.index_fields:
                for obj in cls.query.all():
                    obj.update_index(writer)
        writer.commit()


main = make_main(UpdateIndexesCommand)