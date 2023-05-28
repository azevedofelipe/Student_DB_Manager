# Student Account Class
class StudentAccount:

    _last_assigned_id = 901880000

    # The constructor that initializes the instance variables
    # Creates dictionary with student info based on parameters passed
    def __init__(self, first_name, last_name, admittance_year):
        self.user = {'id': self.set_student_id(), 'first': first_name, 'last': last_name, 'year': admittance_year,
                     'email': first_name[0].lower() + last_name.lower() + str(admittance_year) + '@my.fit.edu'}

        # If user is first 20, uses specific image, else uses generic photo
        if self.user['id'] < 901880021:
            self.user['photo'] = first_name + '_' + last_name + '_' + str(self._last_assigned_id) + '.png'
        else:
            self.user['photo'] = self.set_photo()

    # Incrememnts _last_assigned_id by one everytime new student added to db, assigns id to user
    def set_student_id(self):
        StudentAccount._last_assigned_id = StudentAccount._last_assigned_id + 1

        return StudentAccount._last_assigned_id

    def set_photo(self):
        photo = 'male_silhouette.png'

        return photo
