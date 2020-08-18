from flask import Flask, jsonify, request
from habit import Habit
import json

app = Flask(__name__)

habits = [
        Habit("1").to_dict(),
        Habit("2").to_dict(),
        Habit("3").to_dict(),
]

@app.route("/habits")
def getAll():
    return jsonify(habits)

@app.route("/habits", methods = ["POST"])
def createHabit():

    req = request.get_json()
    h = Habit(req["title"])

    habits.append(h.to_dict())
        
    return h.to_dict(), 201

@app.route("/habits/<int:habitID>", methods = ["GET"])
def getOne(habitID):
    for i in range(len(habits)):
        if habits[i]["id"] == habitID:
            return habits[i], 200
        
    return "", 404

@app.route("/habits/<int:habitID>", methods = ["PUT"])
def updateHabit(habitID):
    req = request.get_json()

    for i in range(len(habits)):
        if habits[i]["id"] == habitID:
            print(habits[i])
            print(req)
            habits[i]["title"] = req["title"] 
            return habits[i], 200
        
    return "", 404

@app.route("/habits/<int:habitID>", methods = ["DELETE"])
def deleteHabit(habitID):
    for i in range(len(habits)):
        if habits[i]["id"] == habitID:
            habits.pop(i)
            return jsonify(habits), 200

    return "", 404
