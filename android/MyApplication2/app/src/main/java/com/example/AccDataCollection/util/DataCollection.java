package com.example.AccDataCollection.util;

import android.content.Context;
import android.content.res.AssetManager;
import android.util.Log;

import java.io.IOException;

public class DataCollection implements Runnable {
    private static volatile DataCollection dataCollection;
    private boolean runningState = false;

    Context context;
    AssetManager assetManager;
    Audio audio;
    Accelerometer accelerometer;


    String audioFolderName = "recordings";
    String accFolderName = "accelerometer_data";

    String[] audioFolderList1;
    String[] audioFolderList2;
    String[] accFolderList1;

    public void pauseThread() {
        runningState = false;
    }

    private DataCollection(Context context) {
        this.context = context;
        assetManager = context.getAssets();
        audio = new Audio(context);
        accelerometer = new Accelerometer(context);


        try {
            audioFolderList1 = assetManager.list(audioFolderName);
            accFolderList1 = assetManager.list(accFolderName);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static DataCollection getInstance() {
        return dataCollection;
    }

    public static DataCollection getInstance(Context context) {
        if (dataCollection == null) {
            dataCollection = new DataCollection(context);
        }
        return dataCollection;
    }

    public void run() {
        runningState = true;

        for (String subFolderName : audioFolderList1) {
            try {
                audioFolderList2 = assetManager.list(audioFolderName + "/" + subFolderName);
            } catch (IOException e) {
                e.printStackTrace();
            }
            Log.d("Sensor", subFolderName);

            for (String fileName : audioFolderList2) {
                if (!runningState) return;

                String audioFullFileName = audioFolderName + "/" + subFolderName + "/" + fileName;

                Log.d("Sensor", audioFullFileName);

                audio.setFileName(audioFullFileName);
                Thread td = new Thread(audio, "Audio");

                accelerometer.start();
                td.start();

                try {
                    Thread.sleep(800);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
                AccelerationData data = accelerometer.end();
                new MyFileWriter(context, accFolderName, subFolderName, fileName, data);
                MyLog.append(fileName);
            }
        }
    }
}
