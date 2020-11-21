package com.hack.accdatarec.util;

import android.content.Context;

import java.io.File;
import java.io.FileWriter;

public class FileManager {
    public void writeFileOnInternalStorage(Context mcoContext, String sFileName, String sBody){
        File dir = new File(mcoContext.getFilesDir(), "acclog");
        if(!dir.exists()){
            dir.mkdir();
        }

        try {
            File gpxfile = new File(dir, sFileName);
            FileWriter writer = new FileWriter(gpxfile);
            writer.append(sBody);
            writer.flush();
            writer.close();
        } catch (Exception e){
            e.printStackTrace();
        }
    }
}
