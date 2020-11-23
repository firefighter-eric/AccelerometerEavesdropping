package com.example.AccDataCollection.util;

public class AccelerationData {
    StringBuilder X;
    StringBuilder Y;
    StringBuilder Z;
    StringBuilder T;

    public AccelerationData() {
        X = new StringBuilder();
        Y = new StringBuilder();
        Z = new StringBuilder();
        T = new StringBuilder();
    }

    public AccelerationData add(long t, float x, float y, float z) {
        T.append(t).append(',');
        X.append(x).append(',');
        Y.append(y).append(',');
        Z.append(z).append(',');
        return this;
    }

    public String getX() {
        return X.toString();
    }

    public String getY() {
        return Y.toString();
    }

    public String getZ() {
        return Z.toString();
    }

    public String getT() {
        return T.toString();
    }
}
