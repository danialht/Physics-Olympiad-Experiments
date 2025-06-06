#include <iostream>
#include <cmath>
#include <iomanip>
#include <ctime>
#include <fstream>
#include <exception>

using namespace std ;

const int INT_INF = 2e9 + 10 ;
const double PI = 3.1415926535 ;
const int MAX_SIZE = 1e3 ;
const double MIU = 4 * PI * 1e-7 ;

long long __time ;

double a = 13.15 , b = 9.21 ;
double center[2] = { 20.50 , 15.58 } ;
double pos[2] = { 0 , 0 } ;
double measure_pos[2] ;
double speed = 30.25 ;
double charge = 107.32 ;
// initial pos = 29.5474 22.2637


calculate_pos( double phi ){
	pos[0] = center[0] + a * cos( phi ) ;
	pos[1] = center[1] + b * sin( phi ) ;
}

void __start_time(){
	__time = clock() ;
}

double __end_time(){
	__time = double ( clock() - __time ) / CLOCKS_PER_SEC ;
}

double size2_of_vector( double a[2] ){
	return a[0] * a[0] + a[1] * a[1] ;
}

double size_of_vector( double a[2] ){
	return sqrt( a[0] * a[0] + a[1] * a[1] ) ;
}

double cross_product_size( double a[] , double b[] ){
	return a[0] * b[1] - a[1] * b[0] ;
}

double calculate_phidot( double phi ){
	double A = a * sin( phi ) ;
	A *= A ;
	double B = b * cos( phi ) ;
	B *= B ;
	return speed / sqrt( A + B ) ;
}

double* calculate_velocity( double phi ){
	static double ret[2];
	double phidot = calculate_phidot( phi ) ;
       	ret[0] = - phidot * a * sin( phi ) ;
	ret[1] = phidot * b * cos( phi ) ;
	return ret ;
}

double calculate_magnetic_field( double phi ){
	double relative_pos[2] = { measure_pos[0] - pos[0] , measure_pos[1] - pos[1] } ;
	double* velocity_arr = calculate_velocity( phi ) ;
	double velocity[2] = { *(velocity_arr) , *(velocity_arr+1) } ;
	//cout << velocity_arr[0] << ' ' << velocity_arr[1] << endl ;
	return MIU * charge * cross_product_size( velocity , relative_pos ) / ( 4 * PI * pow( size_of_vector( relative_pos ) , 3 ) ) ;
}

void run_simulation( double data_B[] , double data_T[] ){
	double phi = PI / 4 ;
	double delta = 0.01 ;
	for(int i = 0 ; i < 1000 ; i++){
		phi += calculate_phidot( phi ) * delta ;
		calculate_pos( phi ) ;
		data_B[i] = calculate_magnetic_field( phi ) ;
		data_T[i] = i * delta ;
		//printing x , y , phi , t
		//printf( "%10.5lf %10.5lf %10.5lf %10.5lf\n" , pos[0] , pos[1] , phi , i * delta ) ;

	}
}

int main(){
	cout << "\n\n I guess this is the last Physics Olympiad Experiment Simulation I ever create in my life...\n Recently things were shitty, therefore I would call this experiment shit hunting...\n    20 July 2023\n    3:57 A.M\n    Danial Hosseintabar\n\n\n" ;
	
	while( true ){
		measure_pos[0] = measure_pos[1] = INT_INF ;
		while( abs(measure_pos[0]) > 50 ){
			cout << "Enter a valid X to put measuring device : " ;
			cin >> measure_pos[0] ;
			if( cin.fail() ){
				measure_pos[0] = INT_INF ;
				cin.clear() ;
				cin.ignore(numeric_limits<streamsize>::max(),'\n');
			}

		}
		while( abs(measure_pos[1]) > 50 ){
			cout << "Enter a valid Y to put measuring device : " ;
			try{
				cin >> measure_pos[1] ;
			} catch( exception& e ) {
				measure_pos[1] = INT_INF ;
				if( cin.fail() ){
					measure_pos[1] = INT_INF ;
					cin.clear() ;
					cin.ignore(numeric_limits<streamsize>::max(),'\n');
					cout << "Error occurred, try again.\n" ;
				}
			}
		}
		
		string name ;
		cout << "enter file name: " ;
		cin >> name ;
		string file_name = name + ".txt" ;
		FILE* file = fopen( &file_name[0] , "w" ) ;

		double data_B[MAX_SIZE] ;
		double data_T[MAX_SIZE] ;

		run_simulation( data_B , data_T ) ;

		fprintf( file , "%9s    %8s\n" , "T ( s )" , "B ( 1e-7 T )" ) ;

		for(int i = 0 ; i < 1000 ; i++)
			if( abs( data_B[i] ) < 4e-4 ) fprintf( file , "%10.5lf %10.5lf\n" , data_T[i] , data_B[i] * 1e7 ) ;
			else fprintf( file , "%10.5lf MAX_LIMIT_EXCEEDED\n" , data_T[i] ) ;

		fclose( file ) ;
	}

}
