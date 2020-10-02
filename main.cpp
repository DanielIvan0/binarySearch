#include <iostream>
#include <vector>
#include <fstream>
#include "Bitacora.hpp"

using namespace std;

vector<Bitacora> cargaBitacora(string archivo);

void Guarda(vector<Bitacora>vec, string archivo, int inicio, int fin) {
    ofstream f;
    f.open(archivo);
    for(int i = inicio; i <= fin; i++) {
        f << vec[i] << endl;
    }
    f.close();
}

void ordenaBurbuja(vector<Bitacora>&lista) {
    bool swap = true;
    int pares = lista.size();

    while (swap) {
        pares--;
        swap = false;
        for (int i = 0; i < pares; i++) {
            if (lista.at(i) > lista.at(i + 1)) {
                Bitacora tmp = lista.at(i);
                lista.at(i) = lista.at(i + 1);
                lista.at(i + 1) = tmp;
                swap = true;
            }
        }
    }
}

int binarySearch(vector<Bitacora>&lista, int l, int r, string x)  { 
    if (r >= l) { 
        int mid = l + (r - l)/2; 
        if (lista[mid].getDate() == x) return mid; 
        if (lista[mid].getDate() > x) return binarySearch(lista, l, mid-1, x);    
        return binarySearch(lista, mid+1, r, x); 
    }
    return -1; 
} 

int main () {
    // Cargamos la bitácora
    vector<Bitacora>bitacora = cargaBitacora("bitacora.txt");
    cout << "---------Bitácora antes de ordenar---------------------" << endl;
    for (auto b : bitacora) {
        cout << b << endl;
    }

    cout << "---------Bitácora después de ordenar-------------------" << endl;
    ordenaBurbuja(bitacora);
    for (auto b : bitacora) {
        cout << b << endl;
        //cout << b.getDate() << endl;
    }

    cout << "---------Búsqueda bitácora----------" << endl;
    string fechaInicial = "153";
    string fechaFinal = "167";
    cout << "Mes inicial: " + fechaInicial << endl;
    cout << "Mes final: " + fechaFinal << endl;
    
    //int inicio = busqBinaria(bitacora, fechaInicial);
    //int final = busqBinaria(bitacora, fechaFinal);

    /*
    if (inicio < 0) {
        inicio = (inicio * -1) - 1;
    }

    if (final < 0) {
        final = (final * -1) - 1;
    }
    */
    
    cout << "---------PRUEBA---------------------" << endl;

    cout << to_string(binarySearch(bitacora, 0, bitacora.size() - 1, fechaInicial)) << endl;
    cout << to_string(binarySearch(bitacora, 0, bitacora.size() - 1, fechaFinal)) << endl;

    fechaInicial = "274";
    fechaFinal = "282";
    cout << "---------PRUEBA---------------------" << endl;
    cout << to_string(binarySearch(bitacora, 0, bitacora.size() - 1, fechaInicial)) << endl;
    cout << to_string(binarySearch(bitacora, 0, bitacora.size() - 1, fechaFinal)) << endl;

    cout << "---------Se ha guardado la bitácora--------------------" << endl;
    //Guarda(bitacora, "bitacoraOK.txt", inicio, final);

    return 0;
}