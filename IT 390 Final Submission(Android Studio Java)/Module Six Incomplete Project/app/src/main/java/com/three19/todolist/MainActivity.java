package com.three19.todolist;
//Cameron Binda
import android.content.Context;
import android.content.DialogInterface;
import android.content.Intent;
import android.support.v7.app.AlertDialog;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.KeyEvent;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ListView;
import android.widget.TextView;

import com.three19.todolist.database.ToDoListDB;
import com.three19.todolist.model.ToDo;

import java.util.ArrayList;
import java.util.List;

public class MainActivity extends AppCompatActivity {

    ToDoListDB toDoListDB;
    List<ToDo> arrayList;
    ToDoListAdapter adapter;
    ToDo selectedToDo;
    int selectedPosition;
    EditText txtName;
    Button addBtn;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        txtName = (EditText) findViewById(R.id.txtName);

        toDoListDB = new ToDoListDB(this);
        arrayList = toDoListDB.getList();

        adapter = new ToDoListAdapter(this, (ArrayList<ToDo>) arrayList);

        ListView listView = (ListView) findViewById(R.id.lstView);
        listView.setAdapter(adapter);
        listView.setOnItemLongClickListener(new AdapterView.OnItemLongClickListener() {
            @Override
            public boolean onItemLongClick(AdapterView<?> arg0, View arg1, int position, long arg3) {
                removeItemFromList(position);
                return true;
            }
        });
        listView.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> parent, View view, int position, long id) {
                selectedToDo = arrayList.get(position);
                selectedPosition = position;
                txtName.setText(selectedToDo.getName());

                addBtn.setText("Update");

            }
        });

        addBtn = (Button) findViewById(R.id.btnAdd);
        addBtn.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                String name = txtName.getText().toString();

                if (!name.trim().isEmpty()) {
                    if (addBtn.getText().equals("Update")) {
                        arrayList.remove(selectedPosition);
                        selectedToDo.setName(name);
                        toDoListDB.update(selectedToDo);

                        arrayList.add(selectedToDo);
                        adapter.notifyDataSetChanged();

                    }
                    else {
                         ToDo toDo = toDoListDB.add(name);
                         arrayList.add(toDo);
                         adapter.notifyDataSetChanged();
                    }
                }
                reset();
            }
        });

        txtName.setOnKeyListener(new View.OnKeyListener() {
            @Override
            public boolean onKey(View view, int i, KeyEvent keyEvent) {
                if (i == KeyEvent.KEYCODE_ENTER) {
                    addBtn.callOnClick();
                    return true;
                }
                return false;
            }
        });

        Button clearBtn = (Button) findViewById(R.id.btnClear);
        clearBtn.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                reset();
            }
        });

        Button allBtn = (Button) findViewById(R.id.btnAll);
        allBtn.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                Intent intent = new Intent(getBaseContext(), AllTasksActivity.class);
                startActivity(intent);
            }
        });

        Button deleteAll = (Button) findViewById(R.id.deleteAll);
        deleteAll.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                deleteAllTasks();
            }
        });
    }

    protected void removeItemFromList(final int position)
    {
        AlertDialog.Builder alert = new AlertDialog.Builder(MainActivity.this);

        alert.setTitle("Delete");
        alert.setMessage("Do you want delete this item?");
        alert.setPositiveButton("YES", new DialogInterface.OnClickListener() {
            @Override
            public void onClick(DialogInterface dialog, int which) {
                ToDo toDo = arrayList.get(position);

                arrayList.remove(position);
                adapter.notifyDataSetChanged();
                adapter.notifyDataSetInvalidated();

                toDoListDB.remove(toDo.getId());
                reset();
            }
        });
        alert.setNegativeButton("CANCEL", new DialogInterface.OnClickListener() {
            @Override
            public void onClick(DialogInterface dialog, int which) {
                dialog.dismiss();
            }
        });

        alert.show();
    }

    protected void deleteAllTasks() {
        AlertDialog.Builder alert = new AlertDialog.Builder(MainActivity.this);

        alert.setTitle("Delete All Tasks?");
        alert.setMessage("Are you sure you want to delete all tasks?");
        alert.setPositiveButton("YES", new DialogInterface.OnClickListener() {
            @Override
            public void onClick(DialogInterface dialog, int which) {
                for (ToDo toDo: arrayList) {
                    toDoListDB.remove(toDo.getId());
                }

                arrayList.clear();
                adapter.notifyDataSetChanged();
                adapter.notifyDataSetInvalidated();
            }
        });

        alert.setNegativeButton("CANCEL", new DialogInterface.OnClickListener() {
            @Override
            public void onClick(DialogInterface dialog, int which) {
                dialog.dismiss();
            }
        });

        alert.show();

    }
    protected void reset() {
        txtName.setText("");
        addBtn.setText("Add");

        selectedToDo = null;
        selectedPosition = -1;
    }
}

class ToDoListAdapter extends ArrayAdapter<ToDo>
{
    public ToDoListAdapter(Context context, ArrayList<ToDo> toDoList) {
        super(context, 0, toDoList);
    }

    @Override
    public View getView(int position, View convertView, ViewGroup parent) {
        ToDo toDo = getItem(position);

        if (convertView == null) {
            convertView = LayoutInflater.from(getContext()).inflate(android.R.layout.simple_list_item_1, parent, false);
        }

        TextView name = (TextView) convertView.findViewById(android.R.id.text1);
        assert toDo != null;
        name.setText(toDo.getName());

        return convertView;
    }
}