package com.example.AccDataCollection.util;

import android.content.Context;
import android.util.Log;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;

public class MyFileWriter {
    public MyFileWriter(Context context, String path1, String path2, String fileName, AccelerationData data) {
//        String state = Environment.getExternalStorageState();
//        if (Environment.MEDIA_MOUNTED.equals(state)) {
//            Log.e("state", "MEDIA_MOUNTED");
//        }


        File dir1 = new File(context.getExternalFilesDir(null), path1);
        if (!dir1.mkdir()) {
            Log.e("Storage", "Directory 1 not created");
        }

        File dir2 = new File(dir1, path2);
        if (!dir2.mkdir()) {
            Log.e("Storage", "Directory 2 not created");
        }


        Log.e("Storage", dir2.toString());
        File file = new File(dir2, fileName + ".txt");
        Log.e("Storage", file.toString());

        try {
            FileOutputStream out = new FileOutputStream(file);
            out.write(data.getT().getBytes());
            out.write("\n".getBytes());
            out.write(data.getX().getBytes());
            out.write("\n".getBytes());
            out.write(data.getY().getBytes());
            out.write("\n".getBytes());
            out.write(data.getZ().getBytes());
            out.write("\n".getBytes());
            out.close();
        } catch (
                IOException e) {
            Log.e("Storage", "IO Error");
            e.printStackTrace();
        }
    }
}
