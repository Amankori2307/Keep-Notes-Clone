from ..models import Notes, MyUser, Label, Media, CheckBox, Collaberator
from ..models import MediaChoices
from .test_setup import TestSetupForModel


class ModelMyUserTestCase(TestSetupForModel):

    def test_model_can_create_a_user(self):
        oldUserCounts = MyUser.objects.all().count()
        user = MyUser(username=self.user_data["username"], email=self.user_data["email"], password=self.user_data["password"])
        user.save()
        newUserCounts = MyUser.objects.all().count()
        self.assertNotEqual(oldUserCounts, newUserCounts)


class ModelNotesTestCase(TestSetupForModel):
    def test_model_can_create_a_notes(self):
        oldNotesCount = Notes.objects.all().count()
        notes = Notes(userRef=self.user)
        notes.save()
        newNotesCount = Notes.objects.all().count()
        self.assertNotEqual(oldNotesCount, newNotesCount)


class ModelLabelTestCase(TestSetupForModel):

    def test_model_can_create_a_label(self):
        oldLabelCount = Label.objects.all().count()
        label = Label(userRef=self.user, name=self.labelName)
        label.save()
        newLabelCount = Label.objects.all().count()
        self.assertNotEqual(oldLabelCount, newLabelCount)


class ModelMediaTestCase(TestSetupForModel):
     
    def test_model_can_create_a_media(self):
        oldMediaCount = Media.objects.all().count()
        media = Media(noteRef=self.note, value=self.value)
        media.save()
        newMediaCount = Media.objects.all().count()
        self.assertNotEqual(oldMediaCount, newMediaCount)

class ModelCheckBoxTestCase(TestSetupForModel):


    def test_model_can_create_a_checkbox(self):
        oldCheckBoxCount = CheckBox.objects.all().count()
        checkBox = CheckBox(noteRef=self.note, text=self.text, status=self.status)
        checkBox.save()
        newCheckBoxCount = CheckBox.objects.all().count()
        self.assertNotEqual(oldCheckBoxCount, newCheckBoxCount)


class ModelCollaberatorTestCase(TestSetupForModel):
    def test_model_can_create_a_checkbox(self):
        oldCollaberatorCount = Collaberator.objects.all().count()
        collaberator = Collaberator(noteRef=self.note, collaberatorRef=self.collaberator)
        collaberator.save()
        newCollaberatorCount = Collaberator.objects.all().count()
        self.assertNotEqual(oldCollaberatorCount, newCollaberatorCount)