def individual_data(Incident):
    return {
        "id" : str(Incident["_id"]),
        "title" : Incident["title"],
        "description" : Incident["description"],
        "status" : Incident["status"],
        "reported_by": Incident["reported_by"]
    }


def all_data(Incidents):
    return [ individual_data(incident) for incident in Incidents]