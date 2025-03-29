my $name = <<'EOF';
%files -n %{python_name}
%{python3_sitelib}/requests_glob-%{version}.dist-info
%{python3_sitelib}/requests_glob.py
%{python3_sitelib}/__pycache__/*
EOF

s/%files -n %{python_name}.*/${name}/g;
