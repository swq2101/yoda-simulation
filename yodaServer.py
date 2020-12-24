from flask import Flask, request, render_template
import yoda_population_simulation

app = Flask(__name__)

currentPopulation = 0
frogsAvailable = 0
mushroomsHarvested = 0

@app.route('/')
def submit_form():
    return render_template('yodaForm.html')


@app.route('/results', methods=['POST'])
def load_form():
    yoda_population_simulation.startingPopulation = int(request.form['startingPopulation'])
    frogsAvalable = int(request.form['frogsHarvested'])
    mushroomsAvailable = int(request.form['mushroomsHarvested'])

    for year in range(0, yoda_population_simulation.millenium):
        currentPopulation = yoda_population_simulation.runYear(yoda_population_simulation.frogsHarvested, yoda_population_simulation.mushroomsHarvested, mushroomsAvailable, frogsAvailable, yoda_population_simulation.fertilityx, yoda_population_simulation.fertilityy, yoda_population_simulation.infantMortality, yoda_population_simulation.deathStarChance)
        print(str(currentPopulation))
    
    templateData = {
        'starting_population': yoda_population_simulation.startingPopulation,
        'current_population': currentPopulation,
        'frogs_available': frogsAvailable,
        'mushrooms_available': mushroomsAvailable
    }   

    return render_template('yodaResult.html', **templateData)



if __name__ == "__main__":
    # Launch the Flask dev server
    app.run(host="localhost", debug=True)