from django.db import models
from django.db import connections


class StudentManager(models.Manager):

    def find(self, matnr):
        """
        Fetch student from external database, return None if id is invalid.
        """
        cursor = connections['faculty'].cursor()
        cursor.execute("select * from student where id = %s", [matnr],)
        row = cursor.fetchone()

        if not row:
            return None

        return Student(id=matnr,
                       first_name=row[1],
                       last_name=row[2],
                       program=row[4])


class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    program = models.CharField(max_length=10)

    objects = StudentManager()

    @property
    def email(self):
        return "{0}@stud.hs-mannheim.de".format(self.id)

    def __str__(self):
        return "{0} {1} ({2})".format(self.first_name,
                                      self.last_name,
                                      self.program)


class Thesis(models.Model):
    title = models.CharField(max_length=200)
    supervisor = models.ForeignKey('Supervisor', on_delete=models.CASCADE)
    assessor = models.ForeignKey('Assessor', on_delete=models.CASCADE)
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    begin_date = models.DateField()
    due_date = models.DateField()

    def __str__(self):
        return "{0}".format(self.title)


class Supervisor(models.Model):
    first_name = models.CharField(max_length=30, verbose_name="Vorname")
    last_name = models.CharField(max_length=30, verbose_name="Nachname")
    id = models.CharField(max_length=30, primary_key=True)

    def __str__(self):
        return "{0} {1} ({2})".format(self.first_name, self.last_name, self.id)

    __repr__ = __str__


class Assessor(models.Model):
    first_name = models.CharField(max_length=30, verbose_name="Vorname")
    last_name = models.CharField(max_length=30, verbose_name="Nachname")
    email = models.EmailField(max_length=80, verbose_name="E-Mail")

    def __str__(self):
        return "{0} {1} ({2})".format(self.first_name,
                                      self.last_name,
                                      self.email)

    __repr__ = __str__