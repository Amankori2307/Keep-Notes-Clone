
def genResponse(error, success, message="", data={}):
    return {
        "error": error,
        "success": success,
        "message": message,
        "data": data
    }
def getNotesForUser(Notes, userRef):
    notes = Notes.objects.filter(userRef=userRef)
    return notes